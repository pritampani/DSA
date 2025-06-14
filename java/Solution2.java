import java.io.*;
import java.util.*;

public class Solution2 {
    public static int get_ans(int N, int M, List<Integer> A) {
        // To store the frequency of elements in A
        int[] freq = new int[M + 1];
        
        // Count the frequency of each element in A
        for (int num : A) {
            if (num <= M) {
                freq[num]++;
            }
        }
        
        // Find the maximum lexicographical subsequence permutation
        List<Integer> P = new ArrayList<>();
        for (int i = M; i >= 1; i--) {
            while (freq[i] > 0) {
                P.add(i);
                freq[i]--;
            }
        }

        // Calculate the required sum
        long sum = 0;
        for (int i = 1; i <= M; i++) {
            sum += (long) P.get(i - 1) * i;
            sum %= 1000000007;
        }
        
        return (int) sum;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = Integer.parseInt(scan.nextLine().trim());
        int M = Integer.parseInt(scan.nextLine().trim());
        List<Integer> A = new ArrayList<>(N);
        
        for (int i = 0; i < N; i++) {
            A.add(Integer.parseInt(scan.nextLine().trim()));
        }

        int result = get_ans(N, M, A);
        System.out.println(result);
    }
}
