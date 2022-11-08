
public class USState {

	private String name;
	private String abbr;
	private int population;
	private String[] neighbors = new String[10];
	private int numneighbors = 0;
	
	
	/**
	 * Constructor - creates an object of type USState
	 */
	public USState(String n, String a)
	{
		this.name = n;
		this.abbr = a;
		checkAbbValid(a);
	}
	
	//********Setter methods**********
	
	/**
	 * Sets the name of this state
	 * parameter: n name of this state
	 */
	public void setName(String n)
	{
		this.name = n;
	
	}
	
	
	/**
	 * Sets the abbreviation of this state
	 * parameter: a abbreviation of this state
	 */
	public void setAbbrev(String a)
	{
		this.abbr = a;
		checkAbbValid(a);	
	}
	
	/**
	 * Sets the population of this state
	 * parameter: p population of this state
	 */
	public void setPopulation(int p)
	{
		this.population = p;
	}
	
	
	/**
	 * Sets the neighbors of this state
	 * parameter: n neighbors of this state
	 */
	public void setNeighbors(String[] n)
	{
		this.neighbors = n;	
	}
	
	
	/**
	 * Sets the number of neighbors of this state
	 * parameter: n number of neighbors of this state
	 */
	public void setNumNeighbors(int n)
	{
		this.numneighbors = n;
	}
	
	
	//********Getter methods**********
	
	/**
	 * Returns the name of this state
	 * return: the name of this state
	 */
	public String getName()
	{
		return this.name;
	}
	
	
	/**
	 * Returns the abbreviation of this state
	 * return: the abbreviation of this state
	 */
	
	public String getAbbrev()
	{
		return this.abbr;
	}
	
	
	/**
	 * Returns the population of this state
	 * return: the population of this state
	 */
	public int getPopulation()
	{
		return this.population;
	}
	
	
	/**
	 * Gets the neighbors of this state
	 * return: neighbors of this state
	 */
	public String[] getNeighbors()
	{
		return this.neighbors;	
	}
	
	
	/**
	 * Gets the number of neighbors of this state
	 * return: number of neighbors of this state
	 */
	public int getNumNeighbors()
	{
		return this.numneighbors;
	}
	
	/**
	 * ToString method
	 */
	public String toString()
	{
		return this.name+" "+this.abbr;	
	}

	//********Other methods**********
	
	/**
	 * Increases the population by given amount
	 * parameter: amt amount to increase population by
	 */
	public void increasePopulation(int amt)
	{
		this.population += amt;
	}

	/**
	 * Decreases the population by given amount
	 * parameter: amt amount to decrease population by
	 */
	public void decreasePopulation(int amt)
	{
		this.population -= amt;
	}

	/**
	 * Checks the validity of the given abbreviation
	 */
	private void checkAbbValid(String ab)
	{
		if(ab.length()!=2)
			System.out.println("invalid abbreviation, please reset");
	}
	
	/**
	 * Adds a new neighbor to the list of neighboring states
	 * param n name of neighbor to add 
	 */
	public void addNeighbor(String n)
	{
		this.neighbors[numneighbors]=n;
		numneighbors++;
	}

	
	
}

