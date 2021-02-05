# helloworldparsl
Parsl example. Run on CRI.

In short, I am trying to run a basic job that takes a file with a single line (hw.txt, with "hello") and dumps it into an output file. The output file is then compressed. 
No parallelism for now.
I am currently running the script by loading up python 3 (i.e. module load python) and running it from the command line on a login node.
The issue I am currently getting is that the job hangs (0 workers connected).
