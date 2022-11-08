
public class BasketballTeamDriver {
	
	public static void main(String[] args) {

		BasketballTeam myTeam = new BasketballTeam("Panthers");
		
		myTeam.addWins(3);
		
		myTeam.addLosses(2);
		
		myTeam.getRecord();
		
		BasketballTeam[] league = new BasketballTeam[5];
		
		league[0] = myTeam;
		
	}

}
