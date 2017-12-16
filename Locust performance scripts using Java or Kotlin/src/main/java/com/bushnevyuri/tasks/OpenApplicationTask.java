package com.bushnevyuri.tasks;

import com.github.myzhan.locust4j.AbstractTask;
import com.github.myzhan.locust4j.Locust;
import com.jayway.restassured.response.Response;

import static com.jayway.restassured.RestAssured.given;

public class OpenApplicationTask extends AbstractTask {
    private int weight;

    public int getWeight() {
        return weight;
    }

    public String getName() {
        return "Open application task";
    }

    public OpenApplicationTask(int weight){
        this.weight = weight;
    }

    @Override
    public void execute() {
        try {
            Response response = given().get("http://blazedemo.com");
            Locust.getInstance().recordSuccess("http", getName(), response.getTime(), 1);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}