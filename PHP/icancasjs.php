<!--
20171230可以正確地將筆資料與時間呈現在網頁
20180306顯示電流線性圖
-->
<!DOCTYPE HTML>
<html>
    <head>
    <script type="text/javascript">
    window.onload = function () {
        var chart = new CanvasJS.Chart("chartContainer",
        {
            zoomEnabled: true,
            title:{
                text: "電流"//標題
            },axisX:{
                title: "時間",//X軸的座標標籤
                gridThickness: 2
            },axisY:{
                includeZero: false//Y軸的座標標籤

            },data:[
                {
                    type: "line",//設定以何種方式呈現資料，在此以線的方式顯示
                    xValueType: "dateTime",//在下方呈現出時間與日期
                    dataPoints:[
                        <?php
                        $servername = "localhost";
                        $username = "root";
                        $password = "openele";
                        $dbname = "power";
                        // Create connection
                        $conn = new mysqli($servername, $username, $password, $dbname);
                        // Check connection
                        if ($conn->connect_error) {
                            die("Connection failed: " . $conn->connect_error);

                        }
                        $sql = "SELECT date, id, i_val FROM auto order by id desc limit 10;";
                        $result = $conn->query($sql);
                        for($i = 0;$i < 11;$i ++) {
                            while($row = $result->fetch_assoc()){
                            echo "{ x: ". $row["date"] ."000, y:". $row["i_val"] .', markerType: "none"},';

                            }
                        }
                        ?>//此PHP是將MySQL中的資料讀取出來並使用陣列
                        ]
                }
                ]// random generator below




        });
        chart.render();

    }
    </script>
    <script type="text/javascript" src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
    <title>電流即時數據圖表</title>
    <meta charset="utf-8">
    <html lang="zh-TW">
    <meta http-equiv="refresh" content="5">
    </head>
    <body>
        <div id="chartContainer" style="height: 300px; width: 100%;">
        </div>
    </body>
</html>
