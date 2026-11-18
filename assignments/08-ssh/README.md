# Assignment 08: Logging Into a Remote Server with SSH

**Due**: Tuesday, November 24 at 11:59 PM on Gradescope

In lecture, we saw how to use SSH to log into a remote machine, set up
key-based authentication, copy files with `scp` and `rsync`, and keep
long-running processes alive with `tmux`. In this assignment, you'll put
those tools to use on the **Data Science / Machine Learning Platform
(DSMLP)** -- the cluster UCSD provides for compute-heavy data science work.

DSMLP isn't a single Linux server -- it's a *cluster* (in particular, it is a
*Kubernetes cluster*, where your jobs run in Docker containers that are scheduled across
many machines; Kubernetes is a system for managing large numbers of Docker
containers). When you SSH in, you land on a small *login node*, but you don't
actually run your work there. Instead, you ask the cluster to launch a Docker
**container** (sometimes called a **pod**) just for you, and your work happens
inside that container. Your home directory is mounted into the container at the
same path, so files you write to `~/something` inside the pod also appear at
`~/something` on the login node.

The goal of this assignment is to take a Python script that runs for about
an hour, get it onto DSMLP, run it there as a long-running job *while you
log out and do something else*, and then retrieve the results. The script we
provide you downloads data about the water temperature at the Scripps Pier
every five minutes for an hour, but you can imagine using the same workflow
to run a long training job, grid search, or any other compute-heavy task.

**What to turn in**: this assignment is a guided tour of DSMLP. As you work
through the steps below, you'll set up SSH key authentication to DSMLP, copy a
Python script onto the cluster, run it as a batch job, and copy the resulting
CSV file back to your machine. At the end, you'll submit that CSV file to
Gradescope. The autograder checks the contents of your CSV against
authoritative data from NOAA.

## Step 1: Log In With Your Password

The DSMLP login node is `dsmlp-login.ucsd.edu`. From your machine, run:

```bash
ssh <your-ad-username>@dsmlp-login.ucsd.edu
```

where `<your-ad-username>` is your UCSD Active Directory username (the same
username you use to log into TritonLink, which is *not necessarily* the same as
your `@ucsd.edu` email address). When prompted, enter your AD password.

Take a quick look around. Run `pwd` and `ls` to see your home directory. Run
`hostname` to see the name of the login node you're on. Notice that you are
*not* yet inside a container -- you are on the shared login node, which is just
an entry point. Don't run any real time-consuming work here (or else campus IT
will be unhappy with you, and, by extension, unhappy with *me*).

When you're done poking around, run `exit` to disconnect.

## Step 2: Set Up SSH Key Authentication

Typing your AD password every time you log in is annoying. Let's set up
key-based authentication instead.

On your **machine** (not on DSMLP), check whether you already have an SSH
keypair:

```bash
ls ~/.ssh/
```

If you see files named `id_ed25519` and `id_ed25519.pub`, you already
have a keypair and can skip ahead. Otherwise, generate one:

```bash
ssh-keygen -t ed25519
```

Accept the default location and leave the passphrase empty (just press
Enter twice). This creates two files in `~/.ssh/`:

- `id_ed25519` -- the **private** key. Never share this.
- `id_ed25519.pub` -- the **public** key. This is the one that goes on
  the server.

Now copy the public key to DSMLP:

```bash
ssh-copy-id <your-ad-username>@dsmlp-login.ucsd.edu
```

You'll be asked for your AD password one last time. Behind the scenes,
`ssh-copy-id` is appending your public key to `~/.ssh/authorized_keys` on
the DSMLP login node.

**Before moving on**: verify that key authentication works. Run

```bash
ssh <your-ad-username>@dsmlp-login.ucsd.edu
```

again. This time, you should *not* be asked for a password. If you are,
something didn't take -- ask for help on Campuswire before continuing.

Exit back to your machine with `exit`.

## Step 3: Add an Alias to Your SSH Config

Typing `<your-ad-username>@dsmlp-login.ucsd.edu` every time is also
annoying. We will add an "alias" so that typing `ssh dsmlp` will log you in.

Open (or create) the file `~/.ssh/config` on your machine and add the following
block:

```
Host dsmlp
    HostName dsmlp-login.ucsd.edu
    User <your-ad-username>
```

Save the file. Now you can log in simply by running:

```bash
ssh dsmlp
```

**Before moving on**: try `ssh dsmlp` and confirm it logs you in with no
password and no extra typing. Exit back to your machine.

## Step 4: Copy the Script to DSMLP

Download `long_job.py` from this repo and save it somewhere sensible on your
machine. Then use `scp` to copy it to your DSMLP home directory.

**Before moving on**: SSH into DSMLP and confirm that `long_job.py` is in your
home directory.

Take a quick look at the script. You'll see that it queries NOAA's tides &
currents API for the current water temperature at the Scripps Pier in La Jolla,
records the reading to a CSV file, sleeps for five minutes, and repeats --
twelve times total. The script takes about an hour to run.

## Step 5: Launch the Script as a Batch Job

This is the key step. We want to start the script on DSMLP and have it
keep running even after we disconnect.

> In lecture, we saw `tmux` as the way to keep a process running after you log
> out of a remote server. On a generic Linux server, `tmux` is still the right
> answer. But DSMLP is a cluster, and it gives us a better tool for the same
> problem: the `launch.sh` script that starts containers on the cluster has a
> `-B` flag for **batch mode**, which launches your container with a script as
> its main process. The job runs independently of your SSH session -- whether
> you're logged in, logged out, or your machine is closed, the job keeps going
> until your script finishes (or until you delete it).

From the DSMLP login node, run:

```bash
launch-scipy-ml.sh -B -- python long_job.py
```

Here are the components of this command:

- `launch-scipy-ml.sh` is the command that asks DSMLP to launch a Docker
  container preloaded with Python and the scientific computing stack. (Other
  launch scripts exist for other images, but this one is fine for us.)
- `-B` tells it to launch the container in **batch mode**: rather than dropping
  you into an interactive shell inside the container, DSMLP runs the command
  you specify as the container's main process and returns control to the login
  node immediately.
- `--` separates `launch-scipy-ml.sh`'s own options from the command you want
  to run inside the container.
- `python long_job.py` is the command you want to run. The script's working
  directory inside the pod will be your home directory (which is mounted in),
  so it'll find `long_job.py` and write `readings.csv` right next to it.

DSMLP will print something like:

```
INFO job was successfully submitted
Please remember to shut down via: "kubectl delete pod <your-username>-NNNN"
You may retrieve output from your pod via: "kubectl logs <your-username>-NNNN"
```

Write down the pod name (`<your-username>-NNNN`). You'll need it later.

## Step 6: Disconnect

Now log out of DSMLP entirely:

```bash
exit
```

Your pod is still running on the cluster -- it doesn't care whether you're
connected. Close your terminal, go grab coffee. Come back in about an hour.

## Step 7: Check on the Job

After roughly an hour, SSH back in to DSMLP. Check on your pod. The `kubectl`
command-line tool is the standard way to talk to a Kubernetes cluster, and
DSMLP has it set up for you.

List your running pods:

```bash
kubectl get pods
```

If your pod is still listed and its `STATUS` is `Running`, the script is
still working -- give it a few more minutes. If the `STATUS` is
`Completed`, your job is done. If the `STATUS` is `Error` or
`CrashLoopBackOff`, something went wrong; see the troubleshooting note
below.

Now look at what the script has printed:

```bash
kubectl logs <your-pod-name>
```

You should see twelve lines of output, one per sample, each showing a
timestamp and a water temperature reading.

## Step 8: Copy the Results Back

The script has been writing to `~/readings.csv` on the *pod*. Because
your home directory is mounted into the pod, this file also lives at
`~/readings.csv` on the *login node*.

Copy the file to your machine with `scp`.

Open `readings.csv` -- it should have a header row and twelve rows of
timestamps and water temperatures in degrees Celsius.

## Step 9: Clean Up

A finished pod doesn't consume any compute, but it still hangs around in
DSMLP's pod list until you delete it. Be a good citizen: SSH back in and
remove it with `kubectl delete pod`:

```bash
kubectl delete pod <your-pod-name>
kubectl get pods   # should no longer show your pod
```

## Step 10: What to Turn In

Submit your `readings.csv` file to Gradescope.

The autograder will:

1. Verify that the file has the expected shape: a header row, followed by
   twelve data rows with `timestamp` and `water_temp_c` columns.
2. Query NOAA's historical endpoint for the Scripps Pier station for the
   time range covered by your timestamps, and verify that the water
   temperatures you recorded match the authoritative values (within a
   small tolerance).
3. Confirm that your timestamps actually span roughly an hour -- so you
   can't just record the same temperature twelve times in quick
   succession.

If any of these checks fail, you can re-run the script and resubmit. The
autograder's tests are public.
