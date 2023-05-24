# ktbunya
Simple scripts to help create an interactive session to run jupyter notebooks using UQ's Bunya/Wiener compute.

Only tested on unix. I don't know anything about windows.

## Installation

In your conda environment (e.g. `test`), make sure you have `jupyter` installed and running `python>=3.10`.
```bash
conda create --name test jupyter "python=3.10"
pip install git+https://www.github.com/tuonglab/ktbunya.git
```

## Usage

Create an interactive session with Bunya's cpu or Wiener's gpu nodes:

### Bunya - CPU only (GPU if you are special)
```bash
# create a simple interactive session with 1 cpu
ixcpu
```

```bash
usage: ixcpu [-h] [--ncpus NCPUS] [--mem MEM] [--mem_per_cpu MEM_PER_CPU]
             [--nodes NODES] [--ntasks NTASKS] [--account ACCOUNT]
             [--walltime WALLTIME] [--job_name JOB_NAME] [--gpu] [--gres GRES]

options:
  -h, --help            show this help message and exit
  --ncpus NCPUS         Number of cpus for job. This is 1 for single core
                        jobs, number of cores for multi core jobs, and 1 for
                        MPI jobs. This can be undertstood as
                        `OMP_NUM_THREADS`.
  --mem MEM             RAM per job given in megabytes (M), gigabytes (G), or
                        terabytes (T). Ask for 2000000M to get the maximum
                        memory on a standard node. Ask for 4000000M to get the
                        maximum memory on a high memory node. Default unit
                        without specifying is in megabytes.
  --mem_per_cpu MEM_PER_CPU
                        Alternative to --mem argument. Only relevant to MPI
                        jobs. Passes to `-mem-per-cpu`.
  --nodes NODES         How many nodes the job will use. Always 1 unless you
                        know what you are doing.
  --ntasks NTASKS       Always 1 unless you know what you are doing. Passes to
                        `--ntasks-per-node`. This is 1 for single core jobs
                        and multi core jobs. This is 96 (or less if single
                        node) for MPI jobs.
  --account ACCOUNT     Account String for your research or accounting group.
                        All Account Strings start with `a_`. Use the `groups`
                        command to list your groups.
  --walltime WALLTIME   Wall time for the session to run (and complete).
  --job_name JOB_NAME   Name of job.
  --gpu                 If passed, submit to gpu queue.
  --gres GRES           GRES syntax. Requires `gpu:[type]:[number]`
```

So, for a typical job where you want something like 24 cores and 32gb of ram, all you need to do is:

```bash
ixcpu --ncpus 24 --mem 32000
```

The default command (just `ixcpu`) runs:
```bash
srun --nodes 1 --ntasks-per-node 1 --job-name interactive_bunya --cpus-per-task 1 --mem 80000 --time 12:00:00 --partition general --account a_di_yu --pty bash
```

You can just tweak this/add on if you require different set up.

### Wiener - GPU only
```bash
# similarly for wiener
ixgpu
```

```bash
usage: ixgpu [-h] [--ncpus NCPUS] [--mem MEM] [--mem_per_cpu MEM_PER_CPU]
             [--nodes NODES] [--ntasks NTASKS] [--walltime WALLTIME]
             [--job_name JOB_NAME] [--gres GRES]

options:
  -h, --help            show this help message and exit
  --ncpus NCPUS         Number of cpus for job. This is 1 for single core
                        jobs, number of cores for multi core jobs, and 1 for
                        MPI jobs. This can be undertstood as
                        `OMP_NUM_THREADS`.
  --mem MEM             RAM per job given in megabytes (M), gigabytes (G),
                        or terabytes (T). Ask for 2000000M to get the
                        maximum memory on a standard node. Ask for 4000000M
                        to get the maximum memory on a high memory node.
                        Default unit without specifying is in megabytes.
  --mem_per_cpu MEM_PER_CPU
                        Alternative to --mem argument. Only relevant to MPI
                        jobs. Passes to `-mem-per-cpu`.
  --nodes NODES         How many nodes the job will use. Always 1 unless you
                        know what you are doing.
  --ntasks NTASKS       Always 1 unless you know what you are doing. Passes
                        to `--ntasks-per-node`. This is 1 for single core
                        jobs and multi core jobs. This is 96 (or less if
                        single node) for MPI jobs.
  --walltime WALLTIME   Wall time for the session to run (and complete).
  --job_name JOB_NAME   Name of job.
  --gres GRES           GRES syntax.
                        phase2.0 nodes: --gres=gpu:tesla-smx2:4
                        phase1.0 nodes: --gres=gpu:tesla:2
                        any(default) nodes: --gres=gpu:1
```

Similarly `ixgpu` just runs:

```bash
srun --nodes 1 --ntasks-per-node 1 --job-name interactive_wiener --cpus-per-task 1 --mem 80000 --time 12:00:00 --partition gpu --gres gpu:1 --pty bash
```

## Launching jupyter notebook from local machine with SSH tunnel
```bash
jpynb
```

Follow the instructions in the console print out to access the notebook.

Default port for `jpynb` (for `bunya`) is  `8883` and `jpynbw` (for `wiener`) is `8884`. You can specify a different port number e.g. `jpynb 1234`.

You may need to copy and paste the token manually on the browser, and login, for this to work.

Basically you just need to first run the ssh tunnel step (only need to run once if you just stay on the same node). Then you just open up your browser and type `http://localhost:${PORT}/` e.g. `http://localhost:8883/` if everything is default. If you want to connect to the notebook directly, copy the link with the token.

You might need to kill your ssh tunnel if you experience some issues e.g. having to switch to a different node or you haven't restarted your local machine for a while.

In which case, you have to do this manually:

```bash
ps aux | grep 8883
kill -9 <pid>
```
where `<pid>` is `51138` in my example below:

```bash
uqztuong         51174   0.0  0.0 408636096   1456 s001  S+    4:37pm   0:00.00 grep 8883
uqztuong         51138   0.0  0.0 409246592   5152   ??  Ss    4:36pm   0:00.04 ssh -N -f -L 8883:bun050.hpc.net.uq.edu.au:8883 uqztuong@bunya.rcc.uq.edu.au
````

Just kill all the `pid` that appear until there's no more.

## Connect VS Code on local machine to jupyter notebook on interactive session on Bunya

Now combining the two above (`ixcpu` and `jpynb`) and interacting with it with VS code, click and watch this video I created on youtube:

[![connecting lVS Code to bunya](https://img.youtube.com/vi/a53CsD-8sHs/0.jpg)](https://www.youtube.com/watch?v=a53CsD-8sHs)

The video is a bit outdated and now you don't need to fuss around with copying and editing the url and token. Just use whatever it says on the prompts when you launch jupyter notebook. It will always be `http://localhost:${PORT}/?token=<somelongtoken>`

## Other useful readings

[UQ's HPC docs](https://github.com/UQ-RCC/hpc-docs)

[How to connect vscode and juypter notebook directly](https://blog.jupyter.org/connect-to-a-jupyterhub-from-visual-studio-code-ed7ed3a31bcb)
