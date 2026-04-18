import { Link } from "react-router-dom";
import { useState } from "react";
import arrow2 from "../../assets/arrow2.png"
import Electronics from "../../assets/Electronics.png"
import Fashion from "../../assets/Fashion.png"
import Home from "../../assets/Home.png"
import Lifestyle from "../../assets/Lifestyle.png"
function Curated (){
    const [activeImage, setActiveImage] = useState(null);
    const images = [
        { id: 1, src: Electronics, alt: "Electronics" },
        { id: 2, src: Fashion, alt: "Fashion" },
        { id: 3, src: Home, alt: "Home" },
        { id: 4, src: Lifestyle, alt: "Lifestyle" },
      ];
    return( 
        <div className="bg-[#F2F3FF] pl-[40px] size-auto">
            <div className="flex flex-row items-center justify-between pt-[96px] pr-[32px] pb-[96px] pl-[32px]">
                <h1 className=" font-black text-[36px] text-[#312E81] leading-[40px] tracking-[0.9px]">Curated Collections</h1>
                <Link to="/login" className=" font-bold text-[16px] text-[#3132ED] leading-[24px] flex flex-row gap-[8px] h-[24px] ">View All Categories <img src={arrow2} alt="Arrow"  className="object-cover w-[15px] h-[15px]"/></Link>
            </div>
        </div>
    )
}
export default Curated;