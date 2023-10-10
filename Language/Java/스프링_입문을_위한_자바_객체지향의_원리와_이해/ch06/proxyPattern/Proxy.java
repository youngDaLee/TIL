package proxyPattern;

public class Proxy implements IService{
    IService service1;

    public String runSomething() {
        System.out.println("호출 흐름 제어... 반환 결과는 그대로 전달");

        // 상황에 따라 다른 구현메서드를 호출하려고 하는건가?
        service1 = new Service();
        return service1.runSomething();
    }
}
