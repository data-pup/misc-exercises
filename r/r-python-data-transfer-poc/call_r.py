import subprocess

def call_r_script(my_param1, my_param2):
    '''Call the R script, using the two given parameters.'''

    try:
        my_param1_s = str(my_param1)
        my_param2_s = str(my_param2)
    except Exception:
        print('Exception while casting input parameters to str().')
        return 1
    else:
        my_argv = ['/usr/local/bin/Rscript', 'print_argv.R', my_param1_s, my_param2_s]
        my_proc = subprocess.run(my_argv)
        my_proc.check_returncode()
        print(my_proc.stdout)
        return my_proc.returncode



def main():
    '''Main runtime function.'''
    call_r_script(1,2)

# If script is invoked directly, run the main function.
if __name__ == '__main__':
    main()
