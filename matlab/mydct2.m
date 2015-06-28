function f = mydct2( F )
% 2D DCT transform
%   Input:
%       F: M-by-N matrix
%   Output:
%       f: M-by-N matrix
%

f = mydct(mydct(F).').';
end

