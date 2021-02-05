from parsl.providers import TorqueProvider
from parsl.channels import LocalChannel
from parsl.config import Config
from parsl.executors import HighThroughputExecutor
from parsl.launchers import SingleNodeLauncher

config = Config(
    executors = [
        HighThroughputExecutor(
            label = "test",
            max_workers = 1,
            
            provider = TorqueProvider(
                launcher=SingleNodeLauncher(),
                account = "mfknie",
                walltime = "10:00:00",
                scheduler_options="#PBS -l mem=8gb -l nodes=1:ppn=2 -N test",
                worker_init = 
                    "\n".join(("module load gcc/6.2.0",
                    "module load pigz")),
                    # "module load miniconda3/4.7.10",
                    # "module load R/4.0.3",
                    # "source activate /gpfs/data/gao-lab/software/local_ancest")),
                nodes_per_block=1,
                init_blocks=1,
                min_blocks=1,
                max_blocks=1,
                # parallelism=1
            )
        )
    ]
)