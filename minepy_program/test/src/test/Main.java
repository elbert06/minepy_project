package Main;

import org.bukkit.block.Block;
import org.bukkit.event.block.Action;
import org.bukkit.Material;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;
import org.bukkit.World;
import java.util.ArrayList;
import org.bukkit.entity.Player;
import org.bukkit.Location;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.event.Listener;
import org.bukkit.Bukkit;
import org.bukkit.event.EventHandler;
import org.bukkit.event.block.BlockBreakEvent;
public class Main extends JavaPlugin implements Listener{
    public Inventory l ;
    ItemStack g = new ItemStack(Material.AIR,1);
    public Material k ;
    public Player m ;
    @Override
    public void onEnable(){
        Bukkit.getPluginManager().registerEvents(this,this);
        System.out.println("plugin enabled"+"");
    }
    @EventHandler
    public void test1(BlockBreakEvent e) {
        m = e.getPlayer();
        m.sendMessage("TEST"+"");
        e.setDropItems(false);
        k = e.getBlock().getType();
        if(!(k.equals(Material.AIR))) {
        	Material.
            g.setType(k);
            g.setAmount(1);
            l = e.getPlayer().getInventory();
            l.addItem(g);
        }
    }
}