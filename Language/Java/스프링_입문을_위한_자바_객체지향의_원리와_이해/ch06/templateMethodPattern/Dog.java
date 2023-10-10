package templateMethodPattern;

public class Dog extends Animal {
    @Override
    void play() {
        System.out.println("멍멍");
    }

    @Override //Hook(갈고리) 오버라이딩~
    void runSomething() {
        System.out.println("멍멍멍ㅁㅁ꼬리살랑~");
    }
}
