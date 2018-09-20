<!DOCTYPE html>

<html>
<head>
    <title>電力參數資料表</title>
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
-->
    <h2>目前插座狀況</h2>
    <?php
    $servername = "127.0.0.1";
    $username = "root";
    $password = "openele";
    $dbname = "power";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT id, date, v_val ,i_val ,p_val ,pt_val ,pf_val  FROM auto order by id desc limit 10;";
    //$sqlid = "SELECT id FROM pi";
    $result = $conn->query($sql);
    //$result1 = $conn1->query($sqlid);
    if ($result->num_rows > 0) {
        // output data of each row
        $i=0;
        echo '<table width="900" border="1">';
        echo '<tr>';
        echo '<td>編號</td>';
        echo '<td>時間</td>';
        echo '<td>電壓</td>';
        echo '<td>電流</td>';
        echo '<td>功率</td>';
        echo '<td>PF</td>';
        echo '</tr>';
        while($row = $result->fetch_assoc()) {
            echo '<tr>';
            echo '<td>'. $row["id"] . '</td>';
            echo '<td>'. date('Y/m/d H:i:s',$row["date"]) . '</td>';
            echo '<td>' . $row["v_val"] . '</td>';
            echo '<td>' . $row["i_val"]. '</td>';
            echo '<td>' . $row["p_val"] .'</td>';
            echo '<td>' . $row["pf_val"] . '</td>';
            echo '</tr>';

            }
        echo '</table>';


    } else {
        echo "0 results";
    }
    $conn->close();

    ?>
</body>
</html>
