# Install
```
module load gcc/6.2.0
module load miniconda3/4.7.10

conda create --name prs python=3.7
# not sure why conda activate doesn't work, even after 'conda init'ing-- something weird at CRI
source activate prs

# probably unnecessary but I prefer to run with latest as there are frequent bug fixes
git clone https://github.com/Parsl/parsl.git
cd parsl
conda install pip
pip install .
```

# Run
(From a head node)
```
module load gcc/6.2.0
module load miniconda3/4.7.10
source activate prs

python test_parsl.py
```

# helloworldparsl
Parsl example. Run on CRI.

## Background
In short, I am trying to run a basic job that takes a file with a single line (hw.txt, with "hello") and dumps it into an output file. The output file is then compressed. 
I am not attempting to do any parallelism for now; I tried to specify the config to use only 1 node/block/worker. I am currently running the script by loading up python 3 (i.e. module load python) and running it from the command line on a login node.  

## Files
* config.py contains the parsl config
* test_parsl.py contains all the apps, as well as the main "driver" code
* hw.txt is an input file that just contains the line "hello"
* test_parsl.pbs is a torque job submission script that I once tried to use to run the code.
 
## Issue
The issue I am currently getting is that the job hangs indefinitely. As seen in the log, after the task is launched, the message `Executor test has 1 active tasks, 0/1 running/pending blocks, and 0 connected workers` begins playing continuously while parsl keeps polling (is this standard while parsl waits in queue?). If I qstat, it shows the corresponding job in Q/queue status.  
  
I think it's possible that this is just CRI having a lot of stuff in queue, but I have run this for several hours earlier in the week. During the same period, I was able to submit jobs with far higher resource requirements, and they ran with no issues.
  
Various things I have tried:
* Fidling with various config parameters, including but not limited to:
  + All the ones related to blocks (init, min, max - lowering the former two to 0, increasing the latter) 
  + Getting rid of max_workers
  + Setting workers_per_node (Does this argument exist? I couldn't find it in the references for Config, the executor or the TorqueProvider - https://parsl.readthedocs.io/en/stable/userguide/execution.html)
* Moving the python code out of `if __name__ == "__main__"`
* Only running the write_hello() app.
