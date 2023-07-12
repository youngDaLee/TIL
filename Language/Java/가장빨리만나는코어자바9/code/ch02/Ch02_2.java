package code.ch02;

import java.util.Random;
import java.util.Scanner;
import java.util.Scanner.*;

/**
 * 2. Scanner 클래스의 nextInt 메서드를 생각해보자. 이 메서드는 접근자인가 변경자인가? 그 이유는? Random 클래스의 nextInt 메서드는 어떤가?
 * Scanner 클래스의 nextInt : 접근자. Scanner를 통해 입력받은 값을 Scanner 객체에 저장하는 것이 아니라, nextInt 메서드 호출 시 리턴하기 때문.
 * Random 클래스의 nextInt : 접근자. 마찬가지로 생성한 랜덤 변수값을 객체에 저장하는 것이 아닌, 매서드 내에서 랜덤 정수를 생성하고 리턴해주는 역할이기 때문
 */
public class Ch02_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Now Print");
        System.out.println(scanner.nextInt());

        Random random = new Random();
        System.out.println(random.nextInt());
        System.out.println(random.nextInt());
    }
}
