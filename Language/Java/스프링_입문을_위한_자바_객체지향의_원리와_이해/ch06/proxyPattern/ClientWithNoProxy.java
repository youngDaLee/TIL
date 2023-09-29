package proxyPattern;

public class ClientWithNoProxy{
    public static void main() {
        Service service = new Service();
        System.out.println(service.runSomething());
    }
}
