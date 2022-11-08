import java.util.ArrayList;

import javax.sound.midi.MidiChannel;

public class QuicksortPrac {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println('a' < 'B');
		
		ArrayList<Integer> test = new ArrayList<Integer>();
		
		for(var v = 0; v < 100; v++) {
			
			test.add(v % 50);
			//System.out.println(v % 10);
			//System.out.println(test);
		}
		
		quicksort(test, 0, test.size() - 1);
		
		System.out.println(test);
		
		
		

	}
	
	
	public static void quicksort(ArrayList<Integer> li, int firstInd, int lastInd){
		
		//System.out.println("FIRSTIND: " + firstInd);
		//System.out.println("LASTIND: " + lastInd);
		
		//System.out.println("2nd El: " + li.get(1));
		
		
		if(lastInd - firstInd <= 2) {
			
			for(var i = 0; i < lastInd - firstInd; i++) {
				int ind = firstInd + i;
				if(li.get(ind) > li.get(ind + 1)) {
					int temp = li.get(ind);
					li.set(ind, li.get(ind + 1));
					li.set(ind + 1, temp);
				}
			}
			
		}else {
		
			int first = li.get(firstInd);
			
			int midInd = (lastInd + firstInd) / 2;
			int mid = li.get(midInd);
			
			int last = li.get(lastInd);
			
			int pivot;
			int pivotLoc;
			
			int[] arr = new int[3];
			arr[0] = first;
			arr[1] = mid;
			arr[2] = last;
			
			
			for(var i = 0; i < arr.length - 1; i++) {
				if(arr[i] > arr[i + 1]) {
					int temp = arr[i];
					arr[i] = arr[i + 1];
					arr[i + 1] = temp;
				}
			}
			//System.out.println("MID: " + mid);
			//System.out.println(arr[0] + " - " + arr[1] + " - " + arr[2]);
			
			pivot = arr[1];
			
			if(arr[1] == first) {
				pivotLoc = firstInd;
			}else if (arr[1] == mid) {
				pivotLoc = midInd;
			}else{
				pivotLoc = lastInd;
			}
			//System.out.println(li);
			//System.out.println(pivot);
			
			int midRange = partition(li, firstInd, lastInd, pivot, pivotLoc);
			
			quicksort(li, 0, midRange - 1);
			//System.out.println("MIDRANGE: " + midRange);
			//System.out.println(li);
			
			quicksort(li, midRange + 1, lastInd);
			
			
		
		}
		
		
	}
	
	public static int partition(ArrayList<Integer> li, int firstInd, int lastInd, int pivot, int pivotLoc) {
		
		li.set(pivotLoc, li.get(lastInd));
		li.set(lastInd, pivot);
		
		int i = firstInd;
		int j = lastInd - 1;
		
		while(i <= j) {
			int iEl = li.get(i);
			int jEl = li.get(j);
			
			//System.out.println("OUT1: " + iEl);
			//System.out.println("OUT2: " + jEl);
			
			if(iEl > pivot && jEl < pivot) {
				//System.out.println("SWAP");
				li.set(i, jEl);
				li.set(j, iEl);
				i++;
				j--;
			}
			
			if(iEl <= pivot) {
				i++;
			}
			
			if(iEl > pivot && jEl >= pivot) {
				j--;
			}
		}
		
		li.set(lastInd, li.get(i));
		li.set(i, pivot);
		//System.out.println(i);
		return i;
		
	}
	

}
