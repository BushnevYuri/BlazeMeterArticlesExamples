package com.bushnevyuri.tasks

import com.github.myzhan.locust4j.AbstractTask
import com.github.myzhan.locust4j.Locust
import com.jayway.restassured.response.Response

import com.jayway.restassured.RestAssured.given

class OpenApplicationKotlinTask(private val weight: Int) : AbstractTask() {

    override fun getWeight(): Int {
        return weight
    }

    override fun getName(): String {
        return "Open application task"
    }

    override fun execute() {
        try {
            val response = given().get("http://blazedemo.com")
            Locust.getInstance().recordSuccess("http", getName(), response.getTime(), 1)
        } catch (ex: Exception) {
            ex.printStackTrace()
        }

    }
}