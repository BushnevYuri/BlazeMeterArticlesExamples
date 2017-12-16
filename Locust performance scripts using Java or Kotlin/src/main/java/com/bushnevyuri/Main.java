package com.bushnevyuri;

import com.bushnevyuri.tasks.FindFlightsTask;
import com.bushnevyuri.tasks.OpenApplicationTask;
import com.github.myzhan.locust4j.Locust;

public class Main {
    public static void main(String[] args) {
        Locust locust = Locust.getInstance();
        locust.setMasterHost("127.0.0.1");
        locust.setMasterPort(5557);

        locust.run(
                new OpenApplicationTask(50),
                new FindFlightsTask(50)
        );
    }
}
