import wamage1 from "../../assets/watch.png";
import shomage2 from "../../assets/sneakers.png";
import glage2 from "../../assets/glass.png";
import headage from "../../assets/headset.png";
import container from "../../assets/Container.png";
function Trending() {
  const props = [
    {
      title: "Architect Chrono V1",
      price: "$299.00",
      img: wamage1,
    },
    {
      title: "Velocity Runner",
      price: "$145.00",
      img: shomage2,
    },
    {
      title: "Eclipse Shade Pro",
      price: "$210.00",
      img: glage2,
    },
    {
      title: "Sonic Aura Wireless",
      price: "$349.00",
      img: headage,
    },
  ];
  return (
    <div>
      <p className="font-bold text-[12px] leading-[16px] tracking-[1.2px] text-[#006C46]  flex justify-center mt-[96px]">
        THE HOT LIST{" "}
      </p>
      <h1 className="font-black text-[48px] leading-[48px] tracking-[-2.4px] text-[#131B2E] flex justify-center pt-[8.5px] mb-[92px]">
        Trending Now
      </h1>
      <section className="grid grid-cols-4 gap-y-[32px] gap-x-[32px] pl-[32px] pr-[32px]">
        {props.map((item, index) => (
          <div
            key={index}
            className="cursor-pointer transition-all duration-300     hover:-translate-y-[5px] hover:shadow-lg"
          >
            <img
              src={item.img}
              alt={item.title}
              className="w-full h-[250px] object-cover rounded-xl"
            />
            <h2 className="mt-[16px] font-bold text-[18px] text-[#131B2E] leading-[28px]">
              {item.title}{" "}
            </h2>
            <p className="mt-[4px] text-[#6B7280] font-medium text-[16px] leading-[24px]">
              {" "}
              {item.price}{" "}
            </p>
          </div>
        ))}
      </section>
      {/* ....CARD...... */}
      <section className="bg-gradient-to-tr from-[#3132ED] to-[#5054FF]  h-[512px]  rounded-[24px] mx-[32px] mt-[96px] mb-[96px] shadow-[0px_25px_50px_-12px_rgba(0,0,0,0.25)] flex relative ">
        {/* LEFT  HAND SIDE */}
        <div className=" flex flex-col  gap-[24px] p-[80px] pr-[0px] ">
          <p className="w-[426px] h-[120px] font-black leading-[65px] text-[#FFFFFF] text-[60px] ">
            20% Off Your First Order{" "}
          </p>
          <p className=" h-[100px] text-[#FFFFFF] font-normal text-[20px] leading-[28px]">
            Start your architectural journey today with an <br />
            exclusive discount across our entire curated <br />
            catalog.
          </p>
          <div className="w-[300px] h-[66px] rounded-[12px] flex gap-[16px] p-[8px] bg-[#FFFFFF1A]  border border-[#FFFFFF33] items-center ">
            <span
              className="font-black text-[#FFFFFF] text-[24px] leading-[32px] px-[16px] font- mono" > ELITE20</span>{" "}
            
              <button className="bg-[#FFFFFF] rounded-[8px] w-[134.13999938964844px] h-[48px] flex items-center justify-center cursor-pointer px-[24px] py-[12px] hover:bg-[#FFFFFFCC] transition duration-300"><span className="text-[#3132ED] font-bold leading-[24px]text-[16px]"> Copy Code</span></button> 
          </div>
        </div>
        {/* RIGHT HAND SIDE */}
        <div className="">
          {" "}
          <img
            src={container}
            alt="Container"
            className=" pt-[40px] object-cover  w-full min-w-[750px] pr -[80px]  ml-[-80px] mr-[-80px]"
          />
        </div>
        <div className="absolute top-16 right-20 w-36 h-34 bg-[#50FCB1] rounded-full blur-[80px]"></div>
      </section>
    </div>
  );
}
export default Trending;
