package templateMethodPattern;

public class Cat extends Animal{
    @Override
    void play() {
        System.out.println("야옹ㅇ");
    }

    @Override //Hook(갈고리) 오버라이딩~
    void runSomething() {
        System.out.println("야오옹옹꼬리살랑~");
    }
}
