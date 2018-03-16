import java.util.Arrays;
import java.util.Scanner;

public class QuizArray {
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int z = 1;
		do{
			System.out.println("How many students would you like to compute the score for?");
			int numStudents = scan.nextInt();
			System.out.println("How many quizes are there?");
			int numQuizes = scan.nextInt();
			
			int[][]quizArray = new int[numStudents][numQuizes];
			
			int classAverage = 0;
			int sum = 0;
			int totalAverage = 0;
			for(int i=0; i<numStudents; i++){
				sum = 0;
				for(int j=0; j<numQuizes; j++){
					System.out.println("What is the score for Student " + (i+1) + " on quiz " + (j+1));
					quizArray[i][j] = scan.nextInt();
					classAverage+=quizArray[i][j];
				}
				for(int h=0; h<numQuizes; h++){
					sum += quizArray[i][h];
					totalAverage +=quizArray[i][h];
				}
				System.out.println("The average for student " + (i+1) + " on the quizes is " + (sum / numQuizes));
			}
			System.out.println("The average for all of the students on all of the quizes is " + (totalAverage / (numQuizes * numStudents)));
			for(int i=0; i<numStudents; i++){
				classAverage = 0;
				for(int j=0; j<numQuizes; j++){
					classAverage+=quizArray[i][j];
				}
				System.out.println("Class average for quiz " + (i+1) + " is " + (classAverage / numStudents));
				
			}
			System.out.println("Continue? [1 = yes, 0 = no]");
			z = scan.nextInt();
		scan.close();
		}
		while(z==1);
		
	}
}
