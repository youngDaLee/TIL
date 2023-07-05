package code.ch01;

public class Ch01_5 {
    /**
     * 5. int의 최댓값보다 큰 double을 int 타입으로 변환하면 무슨 일이 일어나는가? 시도해보자
     * => int의 최댓값이 나오게 됨.
     */
    public static void main(String[] args) {
        double bigDouble = 99999999999999999.999999;
        int doubleToInt = (int) bigDouble;
        System.out.println(doubleToInt);
        // 출력 결과 : 2147483647
    }
}
