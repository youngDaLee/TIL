package code.ch01;

public class Ch01_10 {
    /**
     * 10. 임의의 long값을 생성한 후 36진수로 출력해 임의 글자와 숫자로 구성된 문자열을 만들어내는 프로그램을 작성해라
     */
    public static String longTo36redix(long num) {
        return Long.toString(num, 36);
    }

    public static void main(String[] args){
        longTo36redix(100);
    }
}
