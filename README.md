# ktbunya
Simple scripts to help create an interactive session to run jupyter notebooks using UQ's Bunya/Wiener compute.

Only tested on unix. I don't know anything about windows.

## Installation

In your conda environment (e.g. `test`), make sure you have `jupyter` installed and running `python>=3.10`.
```bash
conda create --name test jupyter "python=3.10"
pip install git+https://www.github.com/zktuong/ktbunya.git
```

## Usage

Create an interactive session with Bunya's cpu or Wiener's gpu nodes:

### Bunya - CPU only
```bash
# create a simple interactive session with 1 cpu
ixcpu
```

```bash
usage: ixcpu [-h] [--ncpus NCPUS] [--mem MEM] [--mem_per_cpu MEM_PER_CPU] [--nodes NODES] [--ntasks NTASKS] [--account ACCOUNT] [--walltime WALLTIME] [--job_name JOB_NAME]

options:
  -h, --help            show this help message and exit
  --ncpus NCPUS         Number of cpus for job. This is 1 for single core jobs, number of cores for multi core jobs, and 1 for MPI jobs. This can be undertstood as `OMP_NUM_THREADS`.
  --mem MEM             RAM per job given in megabytes (M), gigabytes (G), or terabytes (T). Ask for 2000000M to get the maximum memory on a standard node. Ask for 4000000M to get the maximum
                        memory on a high memory node. Default unit without specifying is in megabytes.
  --mem_per_cpu MEM_PER_CPU
                        Alternative to --mem argument. Only relevant to MPI jobs. Passes to `-mem-per-cpu`.
  --nodes NODES         How many nodes the job will use. Always 1 unless you know what you are doing.
  --ntasks NTASKS       Always 1 unless you know what you are doing. Passes to `--ntasks-per-node`. This is 1 for single core jobs and multi core jobs. This is 96 (or less if single node) for MPI
                        jobs.
  --account ACCOUNT     Account String for your research or accounting group. All Account Strings start with `a_`. Use the `groups` command to list your groups.
  --walltime WALLTIME   Wall time for the session to run (and complete).
  --job_name JOB_NAME   Name of job.
```

### Wiener - GPU only
```bash
# same for gpu on wiener, but with additional gres syntax
ixgpu
```

```bash
usage: ixgpu [-h] [--ncpus NCPUS] [--mem MEM] [--mem_per_cpu MEM_PER_CPU] [--nodes NODES] [--ntasks NTASKS] [--account ACCOUNT] [--walltime WALLTIME] [--job_name JOB_NAME] [--gres GRES]

options:
  -h, --help            show this help message and exit
  --ncpus NCPUS         Number of cpus for job. This is 1 for single core jobs, number of cores for multi core jobs, and 1 for MPI jobs. This can be undertstood as `OMP_NUM_THREADS`.
  --mem MEM             RAM per job given in megabytes (M), gigabytes (G), or terabytes (T). Ask for 2000000M to get the maximum memory on a standard node. Ask for 4000000M to get the maximum
                        memory on a high memory node. Default unit without specifying is in megabytes.
  --mem_per_cpu MEM_PER_CPU
                        Alternative to --mem argument. Only relevant to MPI jobs. Passes to `-mem-per-cpu`.
  --nodes NODES         How many nodes the job will use. Always 1 unless you know what you are doing.
  --ntasks NTASKS       Always 1 unless you know what you are doing. Passes to `--ntasks-per-node`. This is 1 for single core jobs and multi core jobs. This is 96 (or less if single node) for MPI
                        jobs.
  --account ACCOUNT     Account String for your research or accounting group. All Account Strings start with `a_`. Use the `groups` command to list your groups.
  --walltime WALLTIME   Wall time for the session to run (and complete).
  --job_name JOB_NAME   Name of job.
  --gres GRES           GRES syntax. phase2.0 nodes: --gres=gpu:tesla-smx2:4 phase1.0 nodes: --gres=gpu:tesla:2 any(default) nodes: --gres=gpu:1
```

### Launching jupyter notebook from local machine with SSH tunnel
```bash
jpynb
```

Follow the instructions in the console print out before the usual jupyter notebook print outs. Scroll up if it happens too quickly.

Default port is `8883`. You can specify a different port number e.g. `jpynb 1234`.

Basically you just need to first run the ssh tunnel step (only need to run once if you just stay on the same node). Then you just open up your browser and type `http://http://localhost:${PORT}/` e.g. `http://http://localhost:8883/` if everything is default.

You might need to kill your ssh tunnel if you experience some issues e.g. having to switch to a different node

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
