import java.io.*;
import java.net.*;

public class ChatClient {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 5000);
            System.out.println("Connected to server!");

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            String messageFromServer, messageToServer;

            while (true) {
                System.out.print("Client: ");
                messageToServer = userInput.readLine();
                out.println(messageToServer);

                if (messageToServer.equalsIgnoreCase("exit")) {
                    System.out.println("Client closed the chat!");
                    break;
                }

                messageFromServer = in.readLine();
                if (messageFromServer.equalsIgnoreCase("exit")) {
                    System.out.println("Server disconnected!");
                    break;
                }
                System.out.println("Server: " + messageFromServer);
            }

            socket.close();
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
