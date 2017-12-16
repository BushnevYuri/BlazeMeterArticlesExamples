package com.bushnevyuri.tasks;

import com.github.myzhan.locust4j.AbstractTask;
import com.github.myzhan.locust4j.Locust;
import com.jayway.restassured.response.Response;

import static com.jayway.restassured.RestAssured.given;

public class FindFlightsTask  extends AbstractTask {
    private int weight;

    @Override
    public int getWeight() {
        return weight;
    }

    @Override
    public String getName() {
        return "Find flights task";
    }

    public FindFlightsTask(int weight){
        this.weight = weight;
    }

    @Override
    public void execute() {
        try {
            Response response =
                    given().parameters(
                            "fromPort", "Paris",
                            "toPort", "Buenos Aires").
                    when().post("http://blazedemo.com/reserve.php");

            assert response.getStatusCode() == 200;

            Locust.getInstance().recordSuccess("http", getName(), response.getTime(), 1);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}