package decoratorPattern;

public class Decorator implements IService{
    IService service;

    public String runSomething() {
        System.out.println("호출에 대한 장식. 클라이언트 반환결과에 장식 더해서 전달");
        service = new Service();
        return "정말 " + service.runSomething();
    }
}
