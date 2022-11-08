import java.util.Scanner;
public class BasketballTeam {
	
	private int numPlayers, wins, losses;
	private String teamName;
	
	public BasketballTeam(String s) {
		this.teamName = s;
	}
	
	public void getNumPlayers(int n) {
		this.numPlayers = n;
	}
	
	public void addWins(int n) {
		this.wins += n;
	}
	
	public void addLosses(int n) {
		this.losses += n;
	}
	
	private int WLRatio() {
		return wins/(losses + wins);
	}
	
	public void getRecord() {
		String record = wins + "-" + losses;
		System.out.println(record);
	}
	
}

