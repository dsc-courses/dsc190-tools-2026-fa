# Picking an AI Subscription

To get the most out of this course, you will need access to an AI coding agent,
such as Anthropic's Claude Code or OpenAI's Codex. In fact, some of the
assignments will *require* you to use an agent. There are many options to
choose from -- some are free and some cost money. We will not require you to
use any specific model or subscription.

Because of the complexity of picking an AI agent, we will walk you through
the options. At a high-level, there are two "paths" you can take, depending
on your preferences:

- **The easy path (free)**. This path is recommended if you just want something
  that "just works", is free, and you don't necessarily care about using the
  latest and greatest models. Here, you'll use
  [OpenCode](https://opencode.ai/). The setup is about as simple as it gets,
  and it costs nothing. The catch is that the free models are decent but not
  best-in-class, and they might go away or change at any time.
- **The cutting-edge path (free or paid)**: This path gets access to more
  capable models, like OpenAI's Codex, Claude Code, or OpenCode's paid plans.
  Several of these options are *also* free (for example, if you already pay for
  ChatGPT Plus, or if you grab the free student credits from OpenAI), but the
  setup involves a few more steps (or a few more dollars).

If you're not sure, start with the easy path -- you can always come back and
set up something more capable later.

## Prerequisite: Install Docker Sandboxes

Regardless of which path you take, you should run coding agents in a sandbox
for security. One of the simplest ways to do this is with Docker Sandboxes
(`sbx`).

**On macOS**, install with Homebrew:

```bash
brew install docker/tap/sbx
```

Note that you might be asked to sign in to Docker when you first run `sbx`.

**On Windows**, follow the instructions for installing `sbx` on Ubuntu at
[GitHub](https://github.com/docker/sbx-releases?tab=readme-ov-file#ubuntu).
Note that you want the *Ubuntu* instructions, not the *Windows* instructions,
since you'll be using `sbx` from inside WSL, not Windows.

You might be asked to sign in to Docker when you first run `sbx`.

**Note**: Docker Sandboxes are very new, and they might have some compatibility
issues with older operating systems. If you are on WSL and you see an error
mentioning "KVM" or "nested virtualization", you might need to enable nested
virtualization in your WSL Settings (search for "WSL Settings" in the Start
menu). Moreover, Docker Sandboxes might not work on Windows 10 or on macOS
versions before Tahoe. If you have trouble getting `sbx` to work, see [Using
Docker Containers as Agent Sandboxes](https://github.com/dsc-courses/dsc190-tools-2026-fa/blob/main/resources/03-docker_container_sandboxes/README.md) for an alternative approach.

## Option 1) The easy path with OpenCode (free)

In the "easy path", you will use OpenCode with free models.

[OpenCode](https://opencode.ai/) is a unified terminal app that can talk to
many different models. Out of the box, it comes with access to a handful of
free models. These models are perhaps not as capable as OpenAI's or Anthropic's
frontier models, but they should be good enough for this class.

A few caveats:

- The free models are *free* for an undetermined amount of time and usage, so
  they might go away during the quarter and you might need to switch to a
  paid option.
- By using the free models, you are implicitly agreeing to let OpenCode collect
  data on your usage, which they use to improve their models (that's how they
  can afford to offer them for free -- they are selling your data).

### Running OpenCode in a sandbox

Assuming you've installed `sbx` as described above, `cd` into the directory
where you want to use OpenCode, and run:

```bash
sbx run opencode
```

This will create a sandbox, install OpenCode, share the current directory with
the sandbox, and configure OpenCode so that it can read and write files within
that sandbox (but not outside of it).

You don't need to log in to OpenCode to use the free models, however, the first
time you run `sbx run opencode`, you may be asked to sign in to *Docker*. Once
OpenCode has started, you may need to choose a model. Type `/models` and hit
enter, then look through the list for a model labeled "Free" on the right side
-- at the time of writing, these are *Big Pickle*, *MiniMax M2.5*, and
*Nemotron 3 Super*, but they change regularly. Pick one and you're ready to go.

That's it -- you can start using OpenCode to work on your assignments. If you
later want to try more capable models, read on.

## Option 2) The cutting-edge path with Codex, Claude Code, etc. (free or paid)

If you want access to more capable models, there are several routes. Pick
whichever matches your situation:

### Option A: You already have a $20/month ChatGPT Plus subscription

If you have the $20/month ChatGPT subscription (as some of you probably do),
then you already have access to
[Codex](https://developers.openai.com/codex/cli), OpenAI's coding agent (note:
free ChatGPT accounts *do not* have permanent access to Codex, but might have
temporary access when OpenAI runs promotions -- you should check).

The Plus subscription comes with a limited amount of Codex usage, but OpenAI's
usage limits are quite liberal, and you should have more than enough for the
quarter. Still, you might want to grab the free OpenAI credits for students
at <https://developers.openai.com/community/students> just to be safe.

See "Running Codex in a sandbox" below for how to set it up.

### Option B: You don't have ChatGPT Plus, but you're OK with using OpenAI

If you don't pay for ChatGPT Plus and you're OK using OpenAI's products, then
you can redeem $100 of free Codex credits for students at
<https://developers.openai.com/community/students>. This will let you use
[Codex](https://developers.openai.com/codex/cli) for free until you run out
of credits, which probably won't happen during the quarter (unless you go on
a coding spree).

See "Running Codex in a sandbox" below for how to set it up.

### Option C: You want better models through OpenCode

Beyond the free models, OpenCode offers a cheap subscription plan called
[OpenCode Go](https://opencode.ai/go), and a pay-as-you-go plan called
[OpenCode Zen](https://opencode.ai/zen).

[OpenCode Go](https://opencode.ai/go) is one of the cheapest coding agent
subscriptions available, at $5 for the first month and then $10/month after
that. *Go* gives you access to a handful of capable (but not quite
best-in-class) models, like GLM-5. Usage is limited, but quite generous.

[OpenCode Zen](https://opencode.ai/zen) is a pay-as-you-go service that
provides access to frontier models, including the latest from OpenAI,
Anthropic, Google and more. You pay for what you use, so it can be cheaper
than a subscription if you don't use AI much, or more expensive if you use
it a lot. The price also [depends](https://opencode.ai/docs/zen/#pricing) on
which model you use. For example, as of March 2026, Qwen3 Coder is $1.50 per
1 million output tokens, while Claude Opus 4.6 is $25. If you use Zen, we
recommend setting monthly usage limits and making sure that auto-reload is
disabled so that you don't accidentally rack up an unexpectedly high bill.

Some people use both OpenCode Go and Zen at the same time -- they use an
expensive but very capable model (like Opus) through Zen to do the planning,
and then use a cheaper model (like GLM-5) through Go to do the actual
implementation. This saves money while still giving good results.

To run OpenCode Go or Zen in a sandbox, you can use the same instructions as for the
free OpenCode models (see "Running OpenCode in a sandbox" above). That is, run:

```bash
sbx run opencode
```

To use Go or Zen, you'll need to log in with your OpenCode account inside the
sandbox. Follow the instructions on the [OpenCode
documentation](https://opencode.ai/docs/providers#opencode).

### Option D: Claude Code

Claude Code is quite good -- it's what I use -- but its cheapest subscription
(the $20/month Claude Pro plan) has quite small usage limits in my
experience, and so it is hard to recommend for a class where we *want* you to
use the AI a lot.

Still, Claude Code with Opus 4.6 is one of the best agentic coding experiences
available at the moment. If you want to try it out, I would recommend signing
up for the $20/month subscription with the expectation that you'll need to
pair it with one of the options above (like OpenCode Go) to get enough usage
for the quarter.

To run Claude Code in a sandbox, run:

```bash
sbx run claude
```

### Running Codex in a sandbox

If you're using OpenAI's models (Options 1 or 2), you will likely want to use
*codex*, OpenAI's terminal app for working with their coding agents. `cd`
into the project that you want to isolate and run:

```bash
sbx run codex
```

This takes care of installing codex and sharing the current directory. On the
first run, you may be asked to determine the network permissions: we recommend
"Allow all" for now.

After a few questions, you'll be dropped inside of `codex` itself. If you type
a message, you'll likely get a "401 Unauthorized" error -- this is because
you haven't yet connected `codex` to your OpenAI account. To do so:

1. Type `/logout` and hit enter. This will quit the sandbox.
2. Run `sbx run codex` again. This time, you should see a sign-in screen with
   several options:
   - If you are using the free OpenAI credits, pick the third option and
     follow the instructions.
   - If you have a ChatGPT Plus subscription, choose the "Sign in with Device
     Code" option (the "Sign in with ChatGPT" option *looks* more relevant,
     but it won't work inside of the sandbox). You will be provided with a
     link: follow it, log in, and follow the instructions. You will likely
     reach an error page saying that you must enable device codes in your
     ChatGPT settings -- if so, go ahead and do so and then repeat this step.

You should now be ready to use `codex` in the sandbox. Note that
(unfortunately) you'll need to repeat this process for every *new* sandbox you
create. However, once you've created a sandbox in a directory, you can reuse
it by running `sbx run codex` from that directory again -- you won't need to
repeat the sign-in process.

Note that you can also use your ChatGPT Plus subscription or free credits in
OpenCode instead of Codex, by following these
[instructions](https://opencode.ai/docs/providers#openai).

## What about local models?

There are a number of free coding agents that you can run locally, on your
own machine, at no cost (well, except for electricity). While these have the
advantage of being free, they are probably not the best choice for most
students. The reason is simple: most people do not have a machine capable of
running a capable model at any reasonable speed. For AI to be useful, it
needs to be somewhat responsive, or else you will avoid using it.

Still, if you're interested in going this route, we recommend using
[ollama](https://ollama.com/) or [LM Studio](https://lmstudio.ai/), which
make it easy to run local models. You can connect either of them to OpenCode
by following the instructions on the
[providers](https://opencode.ai/docs/providers) page of the documentation.
