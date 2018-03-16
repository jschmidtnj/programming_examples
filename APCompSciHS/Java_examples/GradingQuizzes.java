import java.util.Scanner;

public class GradingQuizzes 
{
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		
		int z = 0;
		do{
		System.out.println("How many questions are there on the quiz? ");
		final int numQ = scan.nextInt();
		int[] quizKey = new int[numQ];
		System.out.print("What are the answers for the questions?");
		for(int i = 0; i<quizKey.length; i++)
		{
			quizKey[i] = scan.nextInt();
		}
		System.out.print("What are the responses from the test taker?");
		int[] quizResponses = new int[numQ];
		int numCorrect = 0;
		for(int i = 0; i < numQ; i++)
		{
			quizResponses[i] = scan.nextInt();
			if(quizResponses[i] == quizKey[i])
			{
				numCorrect++;
			}
		}
		System.out.println("Number correct: " + numCorrect);
		System.out.println("Grade: " + ((double)numCorrect / numQ)*100);
		
		System.out.print("Grade another quiz? (y/n)");
		String check = scan.next(); //have next instead of nextLine
		if(check.equals("n"));
			{
				z++;
			}
		
		}
		while(z == 0);
		scan.close();
	}
}
