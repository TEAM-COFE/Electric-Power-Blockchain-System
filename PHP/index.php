<!DOCTYPE html>

<html>
<head>
    <title>電源監控系統</title>
    <meta charset="utf-8">
    <html lang="zh-TW">
    <meta http-equiv="refresh" content="5">

</head>
<body>
<!--
20171216編輯，整理了網頁的架構，讓它變得完整與正確。新增了中文的網站主題，有寫上了「目前狀況」，
並將讀取資料MySQL的資料限制在最新的十筆，新增了最新資料
的編號、日期、時間，之後會加上PHP繪圖，讓它像示波器一樣。
20171223成加上讀取MySQL的時間，並完整地顯示在網頁
20171225成功加上表格將數值以比較好讀的方式呈現在網頁上
20180303成功將程式碼修正可以在網頁顯示資料，可以將目前的數據呈現在上面
20180715將狀態與個別插座顯示
-->
    <h2>目前插座狀況</h2>
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

    $sql = "SELECT id, date, v_val ,i_val ,p_val ,pf_val FROM auto order by id desc limit 1;";
    $sql2 = "SELECT socket_code, appliance, status, overload, noload, ageing FROM status WHERE socket_code = 'x01';";
    $sql3 = "SELECT socket_code, appliance, status, overload, noload, ageing FROM status WHERE socket_code = 'x02';";
    $result = $conn->query($sql);
    $result2 = $conn->query($sql2);
    $result3 = $conn->query($sql3);
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {

            $row2 = $result2->fetch_assoc();
            // output data of each row

            echo '電器:'. $row2["appliance"] .'<br>';
            echo '時間:'. date('Y/m/d H:i:s',$row["date"]) .'<br>';
            echo '電壓:'. $row["v_val"] .'<br>';
            echo '電流:'. $row["i_val"] .'<br>';
            echo '功率:'. $row["p_val"] .'<br>';
            echo '功率因數:'. $row["pf_val"] .'<br>';
            echo "插座編號:". $row2["socket_code"] .'<br>';
            if ($row2["status"] == 2){
                echo '插座狀態:不明'."<br>";
            }else{
                if ($row2["status"] == 1){
                    echo '插座狀態:運作中'."<br>";

                }else{
                    if ($row2["status"] == 0){
                        echo '插座狀態:關機'."<br>";
                    }
                }
            }
            if ($row2["overload"] == 2){
                echo '負載狀態:不明'."<br>";

            }else{
                if ($row2["overload"] == 1){
                    echo '負載狀態:過載'."<br>";

                }else{
                    if ($row2["overload"] == 0){
                        echo '負載狀態:正常'."<br>";

                    }

                }

            }
            if ($row2["noload"] == 2){
                echo '過電狀態:不明'."<br>";

            }else{
                if ($row2["noload"] == 1){
                    echo '過電狀態:有負載'."<br>";

                }else{
                    if ($row2["noload"] == 0){
                        echo '過電狀態:無負載'."<br>";

                    }

                }
            }
            if ($row2["ageing"] == 2){
                echo '老化狀態:不明'."<br>";

            }else{
                if ($row2["ageing"] == 1){
                    echo '老化狀態:已有老化現象'."<br>";

                }else{
                    if ($row2["ageing"] == 0){
                        echo '老化狀態:未出現老化現象'."<br>";

                    }


                }


            }
            $row3 = $result3->fetch_assoc();
            echo '電器:'. $row3["appliance"] .'<br>';
            echo "插座編號:". $row3["socket_code"] .'<br>';
            if ($row3["status"] == 2){
                echo '插座狀態:不明'."<br>";
            }else{
                if ($row3["status"] == 1){
                    echo '插座狀態:運作中'."<br>";

                }else{
                    if ($row3["status"] == 0){
                        echo '插座狀態:關機'."<br>";
                    }
                }
            }
            if ($row3["overload"] == 2){
                echo '負載狀態:不明'."<br>";

            }else{
                if ($row3["overload"] == 1){
                    echo '負載狀態:過載'."<br>";

                }else{
                    if ($row3["overload"] == 0){
                        echo '負載狀態:正常'."<br>";

                    }

                }

            }
            if ($row3["noload"] == 2){
                echo '過電狀態:不明'."<br>";

            }else{
                if ($row3["noload"] == 1){
                    echo '過電狀態:有負載'."<br>";

                }else{
                    if ($row3["noload"] == 0){
                        echo '過電狀態:無負載'."<br>";

                    }

                }
            }
            if ($row3["ageing"] == 2){
                echo '老化狀態:不明'."<br>";

            }else{
                if ($row3["ageing"] == 1){
                    echo '老化狀態:已有老化現象'."<br>";

                }else{
                    if ($row3["ageing"] == 0){
                        echo '老化狀態:未出現老化現象'."<br>";

                    }


                }


            }

        }
    } else {

        echo "0 results";


    }
    $conn->close();

    ?>
</body>
</html>
