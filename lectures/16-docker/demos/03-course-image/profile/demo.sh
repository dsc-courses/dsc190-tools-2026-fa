# Helper to quickly cd into a lecture demo directory.
# Usage: demo 2 3  ->  cd to lecture 02's demo 03

demo() {
  local lec=$(printf "%02d" "$1")
  local dem=$(printf "%02d" "$2")
  local dir=(~/dsc190-*/lectures/${lec}-*/demos/${dem}*/)
  if [ -d "${dir[0]}" ]; then
    cd "${dir[0]}"
  else
    echo "Not found: lecture $1, demo $2"
  fi
}
