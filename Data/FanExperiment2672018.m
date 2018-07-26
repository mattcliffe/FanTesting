clear all; 
clc

fname = 'AlphasenseData_26072018_2.csv';
data = importfile(fname);
dt = datetime(datenum(data.DateTime),'convertfrom','datenum');


figure(1)
clf()
subplot(311)
plot(dt,data.PMr1,'k')
hold on 
plot(dt,data.PMr2,'r')
ylabel('PMr [ug/m3]')
grid('on')

subplot(312)
plot(dt,data.SFR1,'k')
hold on 
plot(dt,data.SFR2,'r')
ylabel('SFR [ml/s]')
grid('on')

subplot(313)
plot(dt,data.FanVoltage)
ylabel('Fan Voltage [V]')
grid('on')

print([fname(1:25),'.png'],'-dpng')