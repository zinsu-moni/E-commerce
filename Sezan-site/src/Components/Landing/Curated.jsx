import { Link } from "react-router-dom";
import arrow2 from "../../assets/arrow2.png";
import Electronics from "../../assets/Electronics.png";
import Fashion from "../../assets/Fashion.png";
import Home from "../../assets/Home.png";
import Lifestyle from "../../assets/Lifestyle.png";
function Curated() {
  const images = [
    { id: 0, src: Electronics, alt: "Electronics" },
    { id: 1, src: Fashion, alt: "Fashion" },
    { id: 2, src: Home, alt: "Home" },
    { id: 3, src: Lifestyle, alt: "Lifestyle" },
  ];
  return (
    <div className="bg-[#F2F3FF] flex flex-col px-[32px] py-[96px] gap-[32px]">
      <section className="flex flex-row justify-between">
        <p className="w-[341.9700012207031px] leading-[40px] text-[#312E81] text-[36px] tracking-[-0.9px] font-black">
          Curated Collections
        </p>
        <div className="flex flex-row gap-[8px] items-center cursor-pointer">
          <Link to="/categories">
            <p className="h-[24px] font-bold text-[#3132ED] leading-[24px] ">
              View All Categories
            </p>
          </Link>
          <img src={arrow2} alt="Arrow" className="w-[15px] h-[15px]" />
        </div>
      </section>
      <section className="grid grid-cols-[1fr_1fr] gap-[24px] ">
        <div>
          <Link to="/">
            <img
              src={images[0].src}
              alt={images[0].alt}
              className="object-cover w-full h-full transition-transform duration-500 hover:-translate-y-[10px]"
            />
          </Link>
        </div>
        <section className="grid grid-rows-[1fr_1fr] gap-[24px] ">
          <div>
            <Link to="/">
              <img
                src={images[1].src}
                alt={images[1].alt}
                className="object-cover w-full h-full transition-transform duration-500 hover:-translate-y-[10px]"
              />
            </Link>
          </div>
          <div className="grid grid-cols-[1fr_1fr] gap-[24px]">
            <Link to="/">
              <img
                src={images[2].src}
                alt={images[2].alt}
                className="object-cover w-full h-full transition-transform duration-500 hover:-translate-y-[10px] "
              />
            </Link>
            <Link to="/">
              <img
                src={images[3].src}
                alt={images[3].alt}
                className="object-cover w-full h-full transition-transform duration-500 hover:-translate-y-[10px] "
              />
            </Link>
          </div>
        </section>
      </section>
    </div>
  );
}
export default Curated;
