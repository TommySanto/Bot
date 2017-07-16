package Discord_Bot.Bot;

import javax.security.auth.login.LoginException;
import net.dv8tion.jda.core.AccountType;
import net.dv8tion.jda.core.JDA;
import net.dv8tion.jda.core.JDABuilder;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.MessageChannel;
import net.dv8tion.jda.core.entities.User;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.exceptions.RateLimitedException;
import net.dv8tion.jda.core.hooks.ListenerAdapter;
 
public class App extends ListenerAdapter {
    public static void main( String[] args ) throws LoginException, IllegalArgumentException, InterruptedException, RateLimitedException {
 
        //Initializes the bot
        JDA jdaBot = new JDABuilder(AccountType.BOT).setToken("MzEzMDU2MTA1MTQ2MDg5NDcy.C_kGFg.r4JL0SM03AEAbPBm09USIeWuQwc").buildBlocking();
        jdaBot.addEventListener(new App());
       
    }
   
    @Override
    public void onMessageReceived(MessageReceivedEvent e) {
       
        //Obtains properties of the received message
        Message objMsg = e.getMessage();
        MessageChannel objChannel = e.getChannel();
        User objUser = e.getAuthor();
       
        //Responds to any user who says "hello"
        if (objMsg.getContent().equals("hello")) {
            objChannel.sendMessage("Hello, " + objUser.getAsMention() +"!").queue();
        }
       
    }
}
