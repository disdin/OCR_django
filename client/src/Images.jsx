import React, { useEffect, useState } from 'react'
import './images.css';


function Images() {
  const [imgInput, setimgInput] = useState(null);
  const [showImg, setshowImg] = useState(false);
  const [loading, setloading] = useState(false);

  useEffect(() => {
    setshowImg(false)
  }, [imgInput]);
  const allImages =
    [
      { id: 1, image: 'static/1.jpg', out: 'static/out1.png' },
      { id: 2, image: 'static/2.jpg', out: 'static/out2.png' },
      { id: 3, image: 'static/3.jpg', out: 'static/out3.png' },
      { id: 4, image: 'static/4.jpg', out: 'static/out4.png' },
      { id: 5, image: 'static/5.jpg', out: 'static/out5.png' },
      { id: 6, image: 'static/6.jpg', out: 'static/out6.png' },
      { id: 7, image: 'static/7.jpg', out: 'static/out7.png' },
      { id: 8, image: 'static/8.jpg', out: 'static/out8.png' },
      { id: 9, image: 'static/9.jpg', out: 'static/out9.png' },
      { id: 10, image: 'static/10.jpg', out: 'static/out10.png' }
    ]
  const [path_clicked, setpath_clicked] = useState("");
  const image_clicked = (item) => {
    setpath_clicked(item.image)
    setimgInput(item)
  }
const checkHandler=()=>{
  setshowImg(false)
  setloading(true)
  var time_rand = Math.floor(Math.random() * (6 - 3 + 1)) + 3;
  console.log(time_rand);
  const timer = setTimeout(() => {
    setloading(false)
    setshowImg(true)
  }, time_rand*1000);
}
  return (
    <div >
      <div className='container_upper'>
        <div className='images'>
          {allImages.map((item) => (
            <div key={item.id} onClick={() => image_clicked(item)} style={{ display: "flex", flexDiretion: "column", justifyContent: "center" }}>
              <img src={item.image} className="image-display" />
            </div>
          ))}

        </div>
        <p style={{ fontWeight: "600" }}>{path_clicked}</p>
      </div>
      {
        imgInput ?
          <div className='lower_div'>
            <div className='image_div'>
              <img src={imgInput.image} className="image_check" />
            </div>
            <button className='run_btn' onClick={checkHandler} >Check</button>
            <div className='image_div'>
              {showImg ? <img className="image_check"  src={imgInput.out}  /> 
              : loading ? <img className='loading_gif' src='static/loading_gif.gif'></img> : <></>}

            </div>
          </div> : <></>
      }
    </div>
  )
}

export default Images
