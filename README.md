# chess-tournament-pairing
This will hopefully turn into a repository of programs related to pairing and simulation for chess tournaments. It will mostly be Swiss pairing and in particular the Dutch system as used by FIDE. However, I may add other systems as well, especially if I move towards simulation.

At least some of the programs use wrappers around [JaVaFo](https://www.rrweb.org/javafo/JaVaFo.htm), by Roberto Ricca. I do not distribute this program. You need to download it from its webpage, extract the jave archive and put "main.jar" in some place accesible to the programs. This program implements Swiss pairing (Dutch system) as described by the FIDE handbook, which can be found [here](https://handbook.fide.com/chapter/C0401202507). You will need a sample TRF(x) file, which can be downloaded from JaVaFo's [advanced user manual page](https://www.rrweb.org/javafo/aum/JaVaFo2_AUM.htm) ([direct link](https://www.rrweb.org/javafo/aum/TRFXSample2.txt)). You can create your own, by referring to TRF16 specifications given [here](https://handbook.fide.com/chapter/C04A), and learning about the extensions described in JaVaFo manual.

You will also need to install Java (JDK) and a number of Python libraries. I install the latter via pip and I recommend this method, rather than installing from scratch or installing system wide libraries. My platform is Debian GNU/Linux. If you use a different platform and needed to tweak things, I would be happy to share your instructions.

Programs
========

JaVaFo-helper.py: A simple wrapper, demonstrating how to pass a string (read in from a file) to JaVaFo routines.