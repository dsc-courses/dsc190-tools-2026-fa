# Shortcut to ask the AI coding assistant a question with conversation memory.
# History is stored in ~/.askhistory as JSON.
# Usage: ask how do I list files?

ask() {
  local question="$*"
  local histfile="$HOME/.askhistory"

  # System context for the AI
  local system="You are helping a student who is learning how to work in the shell. \
Do not run bash commands. Do not modify any files. \
Use only the read, grep, glob, and list tools to explore the filesystem when needed."

  # Build a prompt that includes prior conversation history
  local prompt="$system"$'\n\n'
  prompt+="Here are the student's last 10 shell commands:"$'\n'
  prompt+="$(history 11 | head -10)"$'\n\n'
  if [ -f "$histfile" ]; then
    prompt+="Here is our conversation so far:"$'\n'
    prompt+=$(jq -r '.[] | "Q: \(.question)\nA: \(.answer)\n"' "$histfile")
    prompt+=$'\n'"Now answer this new question: $question"
  else
    prompt+="$question"
  fi

  # Run opencode and capture the response
  local answer
  answer=$(opencode run "$prompt")
  echo "$answer" | bat --language md --plain --paging never

  # Append the Q&A pair to history
  local entry
  entry=$(jq -n --arg q "$question" --arg a "$answer" '{question: $q, answer: $a}')
  if [ -f "$histfile" ]; then
    jq --argjson new "$entry" '(. + [$new])[-15:]' "$histfile" > "$histfile.tmp" && mv "$histfile.tmp" "$histfile"
  else
    echo "[$entry]" > "$histfile"
  fi
}

alias wut='ask "Why did my last command not work?"'
