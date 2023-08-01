import subprocess

pre = '''&control
   calculation = 'scf'
   prefix = 'ge'
   pseudo_dir = './pseudopotentials'
   outdir = './'
   verbosity = 'high'
/

&system
   ibrav = 2
   celldm(1) ='''

post = '''\n   nat = 2
   ntyp = 1
   nbnd = 20
   ecutwfc = 40
   ecutrho = 160
/

&electrons
   diagonalization = 'david'
   mixing_beta = 0.7
   conv_thr = 1e-8
/

ATOMIC_SPECIES
Ge  72.64  ge.pbe-dn-kjpaw_psl.1.0.0.UPF

ATOMIC_POSITIONS crystal
Ge 0.0 0.0 0.0
Ge 0.25 0.25 0.25

K_POINTS automatic
8 8 8 1 1 1'''
a = 10.677

print('a,E')

for i in range(0,230,1):
    
    a = 5 + i/10
    string = pre + str(a) + post

    with open('ge.scf.in', 'w') as file:
        print(string, file=file)

    command = "pw.x < ge.scf.in > ge.scf.out"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    command = "cat ge.scf.out | grep 'total energy  ' | tr -s ' ' | tail -1 | cut -d' ' -f5"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    a_values = []
    energies = []
    a_values.append(a)
    energies.append(result.stdout)

    print(str(a) + ',' + result.stdout.strip())



