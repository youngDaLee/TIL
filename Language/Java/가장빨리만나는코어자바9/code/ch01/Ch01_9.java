package code.ch01;

import java.util.Scanner;

public class Ch01_9 {
    /**
     * 09. s.equals(t) 지만 s!=t인 두 문자열 비교 예시
     *
     * 새롭게 안 사실 : == 으로 String을 비교하면, 메모리에서 동일 객체일때만 true를 반환함.
     * 따라서 "World" == "World" 만 true 일 수 있다.
     * String s1 = "world" , ... 로 별도의 객체로 선언된 순간 false를 반환한다.
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String t = "Hello";

        System.out.println(s.equals(t));
        System.out.println(s==t);
    }
}
