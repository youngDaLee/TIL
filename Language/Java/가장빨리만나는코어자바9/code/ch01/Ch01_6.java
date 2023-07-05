package code.ch01;

import java.math.BigInteger;

public class Ch01_6 {
    /**
     * 6. BigInteger를 사용해 팩토리얼을 계산하는 프로그램을 작성하라. 그리고 프로그램을 사용해 1000!을 계산하라
     */
    public static BigInteger factorial(long num) {
        BigInteger f = BigInteger.ONE;
        for (BigInteger i = BigInteger.ONE; BigInteger.valueOf(num+1).compareTo(i) == 1; i = i.add(BigInteger.ONE)) {
            f = f.multiply(i);
        }
        return f;
    }

    public static void main(String[]args) {
        System.out.println(factorial(1));
    }
}
