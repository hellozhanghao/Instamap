<?php
/**
 * Created by PhpStorm.
 * User: zhanghao
 * Date: 2017/3/27
 * Time: 16:54
 */

//require('vendor/smochin/instagram-php-crawler/src/Crawler.php');
foreach (glob("vendor/*.php")as $filename){
    include $filename;
}


$crawler = new Smochin\Instagram\Crawler();
//$media = $crawler->getMediaByTag('z');
//print $media[1];

$media = $crawler->getMediaByLocation(371570631);
//$media = $crawler->getMediaByTag('singapore');

//$tag = $crawler->getTag('f1');

//echo $media[0].getId();
var_dump($media);