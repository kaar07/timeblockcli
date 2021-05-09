# TimeBlockCLI 
  A terminal based time blocking program written in python.  

  ## Installation
     git clone https://github.com/kaar07/timeblockcli.git/ ~/.timeblock
     sh ~/.timeblock/first.sh
  ## Usage
   - In terminal type ***tblock*** to get into interactive mode with timeblockcli
   - \# appears when the program is expecting a default command.
   - Use the default command ***help*** to get started with.
   - Have fun!

  ## Uninstallation commands
      rm -rf ~/.timeblock
      Also delete every line in bashrc with 'timeblock'.

  ## Troubleshooting

  #### Usage Issues
  Verify usage with instructions.
  Run the program and use the default command ***help*** and check.

  #### File related issues
  The program uses *immutable.txt* file to store and archive the schedules. Try the following:  

    cd ~
    cd .timeblock
    rm immutable.txt
    python gen.py
  
  ##### In case of unresolved issues and bugs, do consider reporting or making a pull request.  
