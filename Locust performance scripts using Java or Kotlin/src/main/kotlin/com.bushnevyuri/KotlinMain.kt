package com.bushnevyuri

import com.bushnevyuri.tasks.FindFlightsKotlinTask
import com.bushnevyuri.tasks.OpenApplicationKotlinTask
import com.github.myzhan.locust4j.Locust

fun main(args: Array<String>) {
    val locust = Locust.getInstance()
    locust.setMasterHost("127.0.0.1")
    locust.setMasterPort(5557)

    locust.run(
            OpenApplicationKotlinTask(50),
            FindFlightsKotlinTask(50)
    )
}
