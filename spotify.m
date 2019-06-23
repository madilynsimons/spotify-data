clc;clear;
M = csvread("ms_listened.csv",1,0);

x = M(:,1);
y = M;
y(:,1) = [];

y = y ./ (1000 * 60);

plot(x, y, 'LineWidth', 2);
legend('Fall Out Boy', 'Paramore', 'Japanese Breakfast', ...
    'The Altogether', 'Muse', 'Patrick Stump', 'The Front Bottoms', ...
    'Halsey', 'Billie Eilish', 'BTS');
title('Music Streaming History', 'FontSize', 12);
xlabel('Day', 'FontSize', 12);
ylabel('Minutes Listened', 'FontSize', 12);