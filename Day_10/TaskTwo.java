/*
ip:-
    now take consecutive 3 elements and sort them and then next three elements
    4 9 8 2 14 3 15 6
    i.e., 1st->4 9 8 => 4 8 9 2 14 3 15 6
    next with the updated one 2nd-> 8 9 2 => 4 2 8 9 14 3 15 6
    and so on
op:-
    4 2 8 3 5 6 9 14
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class TaskTwo{
    public static void main(String[] args) throws IOException {
        BufferedReader read=new BufferedReader(new InputStreamReader(System.in));
        String[] numStrings=(read.readLine()).split(" ");
        int[] numbers=new int[numStrings.length];
        for(int i=0;i<numStrings.length;i++){
            numbers[i]=Integer.parseInt(numStrings[i]);
        }
        int temp;
        for(int i=0;i<(numbers.length)-2;i++){
            if(numbers[i]<numbers[i+1] && numbers[i]<numbers[i+2]){
                if(numbers[i+2]<numbers[i+1]){
                    temp=numbers[i+1];
                    numbers[i+1]=numbers[i+2];
                    numbers[i+2]=temp;
                }
            }
            else if(numbers[i+1]<numbers[i] && numbers[i+1]<numbers[i+2]){
                temp=numbers[i];
                numbers[i]=numbers[i+1];
                numbers[i+1]=temp;
                if(numbers[i+2]<numbers[i+1]){
                    temp=numbers[i+1];
                    numbers[i+1]=numbers[i+2];
                    numbers[i+2]=temp;
                }
            }
            else{
                temp=numbers[i];
                numbers[i]=numbers[i+2];
                numbers[i+2]=temp;
                if(numbers[i+2]<numbers[i+1]){
                    temp=numbers[i+1];
                    numbers[i+1]=numbers[i+2];
                    numbers[i+2]=temp;
                }
            }
        }
        for(int i=0;i<numbers.length;i++){
            System.out.print(numbers[i]+" ");
        }
    }
}