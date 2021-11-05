package Main;

import java.util.ArrayList;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.event.Listener;
import org.bukkit.Bukkit;
import org.bukkit.event.EventHandler;
import org.bukkit.event.entity.PlayerDeathEvent;
import org.bukkit.entity.Player;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
public class Main extends JavaPlugin implements Listener{
    public Player player_1 ;
    public String player_name ;
    public ArrayList<String> g = new ArrayList<>();
    @Override
    public void onEnable(){
        Bukkit.getPluginManager().registerEvents(this,this);
        System.out.println("plugin enabled"+"");
    }
    @EventHandler
    public void test1(PlayerDeathEvent e) {
        player_name = e.getEntity().getName();
        if(g.contains(player_name)) {
            player_1 = e.getEntity();
            player_1.sendMessage("test"+"") ;
        }
    }
    public boolean onCommand(CommandSender sender, Command cmd, String Label, String[] args) {
        if (Label.equalsIgnoreCase("check")) {
            if(!(g.contains("elbert"))) {
                g.add("elbert");
                System.out.println("test_complete"+"");
            }
        }
        return false;
    }
}
