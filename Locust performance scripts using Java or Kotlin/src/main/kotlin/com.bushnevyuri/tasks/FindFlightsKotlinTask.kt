package com.bushnevyuri.tasks

import com.github.myzhan.locust4j.AbstractTask
import com.github.myzhan.locust4j.Locust
import com.jayway.restassured.RestAssured.given

class FindFlightsKotlinTask(private val weight: Int) : AbstractTask() {

    override fun getWeight(): Int {
        return weight
    }

    override fun getName(): String {
        return "Find flights task"
    }

    override fun execute() {
        try {
            val response = given().parameters(
                    "fromPort", "Paris",
                    "toPort", "Buenos Aires").
                    `when`().post("http://blazedemo.com/reserve.php")

            assert(response.getStatusCode() == 200)

            Locust.getInstance().recordSuccess("http", getName(), response.getTime(), 1)
        } catch (ex: Exception) {
            ex.printStackTrace()
        }

    }
}