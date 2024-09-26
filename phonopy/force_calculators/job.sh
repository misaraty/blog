#!/bin/sh
#$ -S /bin/sh
#$ -N mapb_ph_1
#$ -j y
#$ -o ./
#$ -e ./
#$ -cwd
#$ -pe mpi 8
#$ -q large.q

source ~/.bashrc

export MKL_NUM_THREADS=1
export OMP_NUM_THREADS=1

vasp='/usr/local/mpich2_1.5.i13/bin/mpiexec -launcher rsh -n '$NSLOTS' -f '$TMPDIR'/machines /usr/local/vasp5.4.1_intel2013/vasp.5.4.1/bin/vasp_std'

cd ./001 &&
$vasp &&
cd ../002 &&
$vasp &&
cd ../003 &&
$vasp &&
cd ../004 &&
$vasp &&
cd ../005 &&
$vasp &&
cd ../006 &&
$vasp &&
cd ../007 &&
$vasp &&
cd ../008 &&
$vasp &&
cd ../009 &&
$vasp &&
cd ../010 &&
$vasp &&
cd ../011 &&
$vasp &&
cd ../012 &&
$vasp &&
cd ../013 &&
$vasp &&
cd ../014 &&
$vasp &&
cd ../015 &&
$vasp &&
cd ../016 &&
$vasp &&
cd ../017 &&
$vasp &&
cd ../018 &&
$vasp &&
cd ../019 &&
$vasp &&
cd ../020 &&
$vasp &&
cd ../021 &&
$vasp &&
cd ../022 &&
$vasp &&
cd ../023 &&
$vasp &&
cd ../024 &&
$vasp &&
cd ../025 &&
$vasp &&
cd ../026 &&
$vasp &&
cd ../027 &&
$vasp &&
cd ../028 &&
$vasp &&
cd ../029 &&
$vasp &&
cd ../030 &&
$vasp &&
cd ../031 &&
$vasp &&
cd ../032 &&
$vasp &&
cd ../033 &&
$vasp &&
cd ../034 &&
$vasp &&
cd ../035 &&
$vasp &&
cd ../036 &&
$vasp &&
cd ../037 &&
$vasp &&
cd ../038 &&
$vasp &&
cd ../039 &&
$vasp &&
cd ../040 &&
$vasp &&
cd ../041 &&
$vasp &&
cd ../042 &&
$vasp &&
cd ../043 &&
$vasp &&
cd ../044 &&
$vasp &&
cd ../045 &&
$vasp &&
cd ../046 &&
$vasp &&
cd ../047 &&
$vasp &&
cd ../048 &&
$vasp &&
cd ../049 &&
$vasp &&
cd ../050 &&
$vasp &&
cd ../051 &&
$vasp &&
cd ../052 &&
$vasp &&
cd ../053 &&
$vasp &&
cd ../054 &&
$vasp &&
cd ../055 &&
$vasp &&
cd ../056 &&
$vasp &&
cd ../057 &&
$vasp &&
cd ../058 &&
$vasp &&
cd ../059 &&
$vasp &&
cd ../060 &&
$vasp &&
cd ../061 &&
$vasp &&
cd ../062 &&
$vasp &&
cd ../063 &&
$vasp &&
cd ../064 &&
$vasp &&
cd ../065 &&
$vasp &&
cd ../066 &&
$vasp &&
cd ../067 &&
$vasp &&
cd ../068 &&
$vasp &&
cd ../069 &&
$vasp &&
cd ../070 &&
$vasp &&
cd ../071 &&
$vasp &&
cd ../072 &&
$vasp 