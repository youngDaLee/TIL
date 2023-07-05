package code.ch01;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ch01_1 {
    static String BIN = "binary";
    static String OCT = "octal";
    static String HEX = "hex";

    /**
     * 1. 정수를 읽어서 2진수, 8진수, 16진수로 출력하는 프로그램을 작성하라. 읽어온 정수의 역수를 16진 부동소수점수로 출력하라
     */
    public static String intToRadix(int num, String radix) {
        if (radix == BIN) {
            return Integer.toBinaryString(num);
        } else if (radix == OCT) {
            return Integer.toOctalString(num);
        } else if (radix == HEX) {
            return  Integer.toHexString(num);
        } else {
            return "";
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("변환할 정수를 입력하세요");
        Integer num = sc.nextInt();

        List<String> redixList = new ArrayList<>();
        redixList.add(BIN);
        redixList.add(OCT);
        redixList.add(HEX);

        for (String redix : redixList) {
            String redixNum = intToRadix(num, redix);
            System.out.println(redix + ": " + redixNum);
        }

        // 2진수 변환
        String binary = Integer.toBinaryString(num);
        // 8진수 변환
        String octal = Integer.toOctalString(num);
        // 16진수 변환
        String hex = Integer.toHexString(num);

        System.out.println("2진수 : " + binary);
        System.out.println("8진수 : " + octal);
        System.out.println("16진수 : " + hex);
    }
}
